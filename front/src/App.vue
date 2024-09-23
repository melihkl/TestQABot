<template>
  <div class="header">
    <h1>
      Hoşgeldiniz! Test Mühendisliği ile ilgili sorularınızı yazabilirsiniz
    </h1>
  </div>
  <div class="chatbot-container">
    <div class="layout">
      <div class="menu-container">
        <h3>Sorular</h3>
        <ul>
          <li
            v-for="(question, index) in questions"
            :key="index"
            @click="handleQuestionClick(question)"
            class="menu-item"
          >
            {{ question }}
          </li>
        </ul>
      </div>
      <div class="chat-area">
        <div class="chat-output" ref="chatOutput">
          <div v-for="message in messages" :key="message.id" class="message">
            <p class="message-text">{{ message.text }}</p>
            <div v-if="message.suggestions && message.suggestions.length">
              <p>İlgili Konular:</p>
              <ul>
                <li
                  v-for="(suggestion, index) in message.suggestions"
                  :key="index"
                  @click="handleSuggestionClick(suggestion)"
                  class="suggestion-item"
                >
                  {{ suggestion }}
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="input-container">
          <input
            v-model="userInput"
            @keyup.enter="sendMessage"
            placeholder="Sorunuzu yazın..."
            class="chat-input"
          />
          <div class="button-container">
            <button @click="sendMessage">Gönder</button>
            <button @click="clearChat" class="clear-button">Temizle</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      userInput: "",
      messages: [],
      questions: [], // Soruların listesi
    };
  },
  async created() {
    try {
      const response = await axios.get("http://localhost:8000/questions");
      this.questions = response.data.questions;
    } catch (error) {
      console.error("Sorular yüklenirken bir hata oluştu:", error);
    }
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === "") return;

      const newMessage = { text: this.userInput, id: Date.now() };
      this.messages.push(newMessage);

      try {
        const response = await axios.post("http://localhost:8000/ask", {
          text: this.userInput,
        });
        this.messages.push({
          text: response.data.answer,
          suggestions: response.data.suggestions || [],
          id: Date.now(),
        });
      } catch (error) {
        this.messages.push({
          text: "Maalesef, bu soruya yanıt bulamadık.",
          id: Date.now(),
        });
      }

      this.userInput = "";
      this.$nextTick(() => {
        const chatOutput = this.$refs.chatOutput;
        chatOutput.scrollTop = chatOutput.scrollHeight;
      });
    },
    async handleQuestionClick(question) {
      this.userInput = question;
      await this.sendMessage();
    },
    async handleSuggestionClick(suggestion) {
      this.userInput = suggestion;
      await this.sendMessage();
    },
    clearChat() {
      this.messages = [];
      this.userInput = "";
    },
  },
};
</script>

<style>
.chatbot-container {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
  display: flex;
}

.header {
  padding: 10px;
  background-color: #007bff;
  color: white;
  text-align: center;
  font-size: 14px;
  font-weight: bold;
}

.layout {
  display: flex;
  width: 100%;
}

.menu-container {
  width: 200px;
  border-right: 1px solid #ccc;
  padding-right: 20px;
  background-color: #fff;
  height: 100vh;
  overflow-y: auto;
}

.menu-item {
  cursor: pointer;
  color: #007bff;
  text-decoration: underline;
  font-weight: bold;
}

.menu-item:hover {
  text-decoration: none;
}

.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.chat-output {
  margin-bottom: 20px;
  max-height: calc(100vh - 140px);
  overflow-y: auto;
}

.message {
  margin-bottom: 10px;
}

.message-text {
  font-size: 16px;
  font-weight: bold;
}

.suggestion-item {
  cursor: pointer;
  color: #007bff;
  text-decoration: underline;
}

.suggestion-item:hover {
  text-decoration: none;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button-container {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.chat-input {
  width: calc(100% - 100px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 80px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.clear-button {
  background-color: #dc3545;
}
</style>

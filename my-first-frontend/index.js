"use strict";
// import * as dotenv from "dotenv"
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// dotenv.config()
class EventsProcessorClient {
    constructor(base_url, username, password) {
        this.base_url = base_url;
        this.username = username;
        this.password = password;
    }
    getResponse() {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const response = yield fetch(this.base_url, {
                    method: "POST",
                    mode: "no-cors",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: "Basic " + btoa(`${this.username}:${this.password}`)
                    },
                    body: JSON.stringify({ message: "Payload enviado do TypeScript" })
                });
                if (!response.ok) {
                    throw new Error("Erro na requisição: " + response.statusText);
                }
                const data = yield response.json();
                return JSON.stringify(data, null, 2);
            }
            catch (error) {
                console.error("Erro:", error);
                return "Erro ao processar a requisição";
            }
        });
    }
    // Método para exibir a resposta no HTML
    displayResponse() {
        return __awaiter(this, void 0, void 0, function* () {
            const message = yield this.getResponse();
            const payloadDiv = document.getElementById("payload");
            if (payloadDiv) {
                payloadDiv.innerText = message; // Define o texto da div
            }
        });
    }
}
const url = "https://datadog-events-processor-958005000987.us-central1.run.app/webhook";
const username = "datadog-events-processor@ivdatahub.com.br";
const password = "b17399c8-8315-466e-a5be-1821b2515433";
const new_event = new EventsProcessorClient(url, username, password);
window.sendPostRequest = () => new_event.displayResponse();

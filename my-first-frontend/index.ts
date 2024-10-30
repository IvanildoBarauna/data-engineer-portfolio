// import * as dotenv from "dotenv"

// dotenv.config()

class EventsProcessorClient {
  constructor(
    private base_url: string,
    private username: string,
    private password: string
  ) {}

  async getResponse(): Promise<string> {
    try {
      const response = await fetch(this.base_url, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Basic " + btoa(`${this.username}:${this.password}`)
        },
        body: JSON.stringify({ message: "Payload enviado do TypeScript" })
      })

      if (!response.ok) {
        throw new Error("Erro na requisição: " + response.statusText)
      }

      const data = await response.json()
      return JSON.stringify(data, null, 2)
    } catch (error) {
      console.error("Erro:", error)
      return "Erro ao processar a requisição"
    }
  }

  // Método para exibir a resposta no HTML
  async displayResponse(): Promise<void> {
    const message = await this.getResponse()
    const payloadDiv = document.getElementById("payload")
    if (payloadDiv) {
      payloadDiv.innerText = message // Define o texto da div
    }
  }
}

const url =
  "https://datadog-events-processor-958005000987.us-central1.run.app/webhook"
const username = "datadog-events-processor@ivdatahub.com.br"
const password = "b17399c8-8315-466e-a5be-1821b2515433"

const new_event = new EventsProcessorClient(url, username, password)

// Define `sendPostRequest` no escopo global
;(window as any).sendPostRequest = () => new_event.displayResponse()

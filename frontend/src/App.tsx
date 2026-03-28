import { useState } from "react";
import { TextInput, Button, Container, Stack, Paper } from "@mantine/core";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState<string[]>([]);

  const sendMessage = async () => {
    if (!message) return;

    try {
      const res = await axios.post("http://localhost:8000/chat", {
        message: message,
      });

      setChat((prev) => [
        ...prev,
        "You: " + message,
        "Bot: " + res.data.response,
      ]);

      setMessage("");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container size="sm" mt="xl">
      <Stack>
        <Paper p="md" shadow="xs" style={{ minHeight: 200 }}>
          {chat.map((msg, index) => (
            <div key={index}>{msg}</div>
          ))}
        </Paper>

        <TextInput
          placeholder="Type your message..."
          value={message}
          onChange={(e) => setMessage(e.currentTarget.value)}
        />

        <Button onClick={sendMessage}>Send</Button>
      </Stack>
    </Container>
  );
}

export default App;
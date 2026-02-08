import { useState } from "react";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const runAgents = async () => {
    if (!topic.trim()) return;

    setLoading(true);
    setOutput("");   // clear old output

    try {
      const res = await fetch("http://127.0.0.1:8000/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic })
      });

      const data = await res.json();
      setOutput(data.output || "No output received");

    } catch (err) {
      setOutput("Backend error: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h1>Multi-Agent Research Assistant</h1>

      <input
        style={styles.input}
        placeholder="Enter research topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button style={styles.button} onClick={runAgents}>
        Run Agents
      </button>

      {loading && <p style={styles.running}>Running agents...</p>}

      {output && (
        <pre style={styles.outputBox}>
          {output}
        </pre>
      )}
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    background: "#121212",
    color: "white",
    padding: "40px",
    fontFamily: "Arial"
  },
  input: {
    padding: "12px",
    width: "400px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "none",
    marginBottom: "15px"
  },
  button: {
    display: "block",
    padding: "10px 18px",
    background: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer"
  },
  running: {
    marginTop: "20px",
    color: "orange"
  },
  outputBox: {
    marginTop: "25px",
    background: "#1e1e1e",
    padding: "20px",
    borderRadius: "6px",
    whiteSpace: "pre-wrap"
  }
};

export default App;

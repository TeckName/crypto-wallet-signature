const backendUrl = "http://localhost:5000";

async function generateWallet() {
  const res = await fetch(`${backendUrl}/wallet`);
  const data = await res.json();
  document.getElementById("publicKey").textContent = data.public_key;
  document.getElementById("privateKey").textContent = data.private_key;

  // Autofill for signing
  document.getElementById("signPrivateKey").value = data.private_key;
  document.getElementById("verifyPublicKey").value = data.public_key;
}

async function signMessage() {
  const message = document.getElementById("message").value;
  const privateKey = document.getElementById("signPrivateKey").value;

  const res = await fetch(`${backendUrl}/sign`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, private_key: privateKey })
  });

  const data = await res.json();
  document.getElementById("signature").textContent = data.signature;

  // Autofill for verify
  document.getElementById("verifyMessage").value = message;
  document.getElementById("verifySignature").value = data.signature;
}

async function verifySignature() {
  const message = document.getElementById("verifyMessage").value;
  const signature = document.getElementById("verifySignature").value;
  const publicKey = document.getElementById("verifyPublicKey").value;

  const res = await fetch(`${backendUrl}/verify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, signature, public_key: publicKey })
  });

  const data = await res.json();
  document.getElementById("verifyResult").textContent = data.valid ? "✅ Doğrudur" : "❌ Yanlışdır";
}

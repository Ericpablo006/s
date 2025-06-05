document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  // Autenticação simples (em ambiente real, usar backend seguro)
  if (user === "admin" && pass === "1234") {
    localStorage.setItem("user", user); // salva no navegador
    window.location.href = "main.html"; // redireciona
  } else {
    document.getElementById("error").textContent = "Usuário ou senha inválidos!";
  }
});
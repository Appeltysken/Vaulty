const form = document.getElementById('loginForm');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = {
    username: form.username.value,
    password: form.password.value
  };
  const res = await fetch('/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
  const json = await res.json();
  document.getElementById('result').textContent = json.message || "";
  if (res.ok && json.redirect) {
    window.location.href = json.redirect;
  }
});

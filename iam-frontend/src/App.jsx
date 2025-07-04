import React, { useState } from 'react'

function App() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [token, setToken] = useState(null)
  const [error, setError] = useState(null)

  async function handleSubmit(e) {
    e.preventDefault()
    setError(null)

    const formData = new URLSearchParams()
    formData.append('username', username)
    formData.append('password', password)

    try {
      console.log(formData.toString)
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
      })

      if (!response.ok) {
        const data = await response.json()
        setError(data.detail || 'Login failed')
        return
      }

      const data = await response.json()
      setToken(data.access_token)
      // Optionnel: stocker token localement
      localStorage.setItem('token', data.access_token)
    } catch (err) {
      setError('Network error')
    }
  }

  return (
    <div style={{ maxWidth: 400, margin: 'auto', padding: 20 }}>
      <h1>Login</h1>
      {token ? (
        <div>
          <p>Login successful! Your token:</p>
          <textarea
            readOnly
            value={token}
            rows={5}
            style={{ width: '100%' }}
          />
        </div>
      ) : (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Username</label>
            <input
              type="text"
              value={username}
              onChange={e => setUsername(e.target.value)}
              required
              autoComplete="username"
            />
          </div>
          <div style={{ marginTop: 10 }}>
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
              autoComplete="current-password"
            />
          </div>
          {error && (
            <p style={{ color: 'red' }}>{error}</p>
          )}
          <button type="submit" style={{ marginTop: 10 }}>
            Login
          </button>
        </form>
      )}
    </div>
  )
}

export default App

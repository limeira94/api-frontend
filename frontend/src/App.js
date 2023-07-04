import React from 'react';
import Blog from './Blog'; // Importe o componente Blog, se ele estiver em um arquivo separado.

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Meu Blog</h1>
      </header>
      <Blog /> {/* Renderize o componente Blog aqui. */}
    </div>
  );
}

export default App;
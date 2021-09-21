import logo from './logo.svg';
import './App.css';
import MainPage from './Main';


// Method that renders main page
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://github.com/m-godlewski/lyrium"
          target="_blank"
          rel="noopener noreferrer"
        >
          Lyrium
        </a>
        <MainPage />
      </header>
    </div>
  );
}

export default App;

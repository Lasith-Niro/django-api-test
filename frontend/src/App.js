import React, { Component } from 'react';
import './App.css';
import StoryContainer from './components/StoryContainer'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App header">
          <h1>Story Board</h1>
        </div>
        <StoryContainer />
      </div>
    );
  }
}

export default App;

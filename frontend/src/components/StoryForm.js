import React, { Component } from 'react';

const data = {
  story: {
    title: '',
    content: '',
    rating:''
  }
}


export default class storyForm extends Component {

  constructor(props) {
    super(props)

    this.state = {
      title: this.props.story.fields.title,
      content: this.props.story.fields.content,
      rating : this.props.story.fields.rating,
    }
  }

  handleInput = (event) => {
    this.props.resetNotification()
    this.setState({
      [event.target.name]: event.target.value
    })
    // console.log(this.state)
    
  }

  handleBlur = () => {
    data.story = {
      title: this.state.title,
      content: this.state.content,
      rating:this.state.rating
    }
    console.warn(data.story);
    this.props.updateStoryRatings(data)
  }

  render() {
    return (
      <div className="big-tile">
        <h4>{this.state.title}</h4>
        <p>{this.state.content}</p>
        <br/>
        <form onBlur={this.handleBlur}>
          <input className='input' type='text' name='rating' placeholder='Enter ratings for story...'  onChange={this.handleInput} />
          <br />
        </form>

      </div>
    )
  }
}

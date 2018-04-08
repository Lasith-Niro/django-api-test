import React, { Component } from 'react';
import StoryAdapter from '../adapters/StoryAdapter'
import Story from './Story'
import StoryForm from './StoryForm'

const data = {
  story: {
    title: '',
    content: '',
    rating:''
  }
}

export default class StoryContainer extends Component {
  constructor(props) {
    super(props)

    this.state = {
      stories: [],
      currentSceneId: null,
      notification: ''
    }
  }

  componentDidMount() {
    StoryAdapter.index()
      .then(json => this.setState({
        stories: json
        },
            () => {console.log(this.state.stories)})
      )
  }

  addNewScene = () => {
    StoryAdapter.create(data)
      .then(json => this.setState({
        stories: [json, ...this.state.stories],
                      currentSceneId: json.id,
                      notification: ''
                    })
      )
  }

  getSceneIndex = (id) => {
    return this.state.stories.findIndex(story => story.id === id)
  }

  updateStoryRatings = (data) => {
    console.log(data);
    StoryAdapter.update(this.state.currentSceneId, this.state.data.rating)
      .then(json => {
                      let index = this.getSceneIndex(json.pk)
                      this.setState({
                        stories: [...this.state.stories.slice(0, index), json, ...this.state.stories.slice(index + 1)],
                        currentSceneId: json.pk,
                        notification: 'All changes saved.'
                      },
                        () => {console.log(this.state.stories)}
                      )
      })
  }

  resetNotification = () => {
    this.setState({
      notification: ''
    })
  }

  enableEditing = (id) => {
    this.setState({
      currentSceneId: id
    })
  }

  render() {
    return (
      <div className="Scenes-container">
        <div className="Scenes-container controls">
          <span className="Scenes-container notification">
            {this.state.notification}
          </span>
        </div>
        <div className="Scenes-container body">
          {this.state.stories.map((story) => {
            return (
              (this.state.currentSceneId === story.pk) ?
              <StoryForm key={story.pk} story={story} resetNotification={this.resetNotification} updateStoryRatings={this.updateStoryRatings} /> :
              <Story key={story.pk} story={story} onClick={this.enableEditing}/>
            )
          })}
        </div>
      </div>
    );
  }
}

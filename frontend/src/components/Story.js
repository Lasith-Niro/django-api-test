import React, { Component } from 'react';

export default class Story extends Component {

  handleClick = () => {
    this.props.onClick(this.props.story.pk)
  }

  // handleDelete = () => {
  //   this.props.onDelete(this.props.scene.pk)
  // }

  render() {
    return (
      <div className="tile">
        <span>{this.props.story.fields.created_at}</span>
        <h4 onClick={this.handleClick}>{this.props.story.fields.title}</h4>        
      </div>
    )
  }
}

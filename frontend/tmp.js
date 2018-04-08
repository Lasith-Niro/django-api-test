<form onBlur={this.handleBlur}>
          <input className='input' type='text' name='title' placeholder='Enter title for story...' value={this.state.title} onChange={this.handleInput} ref={this.props.titleRef} />
          <br />
          <br />
          <textarea className='input' type='text' name='content' placeholder='Describe the story...' value={this.state.content} onChange={this.handleInput} ></textarea>
        </form>
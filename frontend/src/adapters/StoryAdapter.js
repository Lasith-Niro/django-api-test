const baseUrl = 'http://localhost:8000/stories/'
const subUrl = 'http://127.0.0.1:8000/story'
const requestHeaders = {
  'content-type': 'application/json',
  'accept': 'application/json'
}

export default class StoryAdapter {

  static create(data) {
    return (
      fetch(`${baseUrl}`, {
        method: 'post',
        headers: requestHeaders,
        body: JSON.stringify(data)
      })
       .then(resp => resp.json())
    )
  }

  static index() {
    return (
      fetch(`${baseUrl}`)
        .then(resp => resp.json())
    )
  }

  static update(storyID, newRate){
    return (
      fetch(`${subUrl}/${storyID}/update/${newRate}`)
      .then(resp => resp.json())
    )
  }

  // static update(sceneId, data) {
  //   return (
  //     fetch(`${baseUrl}/${sceneId}`, {
  //       method: 'put',
  //       headers: requestHeaders,
  //       body: JSON.stringify(data)
  //     })
  //       .then(resp => resp.json())
  //   )
  // }

  static delete(sceneId, data) {
    return (
      fetch(`${baseUrl}/${sceneId}`, {
        method: 'delete'
      })
        .then(resp => resp)
    )
  }

}

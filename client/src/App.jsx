import { useState } from 'react'
import './App.css'
import {NavBar} from './nav.jsx'
import Axios from 'axios'
import Result from './Result.jsx'

function App() {
  const [formData, setFormData] = useState(() => {
    url: ''
  })
  const [load, setLoad] = useState(false);
  const [data, setData] = useState(null);

  const onChange = (e) => {
    setFormData((prevData) => {
      return {...prevData, [e.target.id]: e.target.value}
    })
  }

  const onSubmit = (e) => {
    setLoad((prevState) => ! prevState)
    e.preventDefault()
    console.log(formData.url)
    Axios.post('http://127.0.0.1:5000/compute', formData)
    .then(response => {
      console.log(response)
      setLoad((prevState) => ! prevState)
      setData(response.data)
    })
    .catch(error => {
      console.error('error:', error)
    })

  }

  return (
    <>
      <NavBar />
      <form onSubmit={onSubmit}>
        <input onChange={(e) => onChange(e)} id='url' type='text' placeholder='Enter Url'></input>
        <input  id='submitBtn' type="submit" value='Submit'/>
      </form>
      {load ? <p>Loading...</p> : data ? 
      <>
      <Result data={data} />
      </> : <></>}
    </>
  )
}

export default App

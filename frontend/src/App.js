import { useEffect, useState } from "react";
import Axios from "axios";
import Css from './Css.css'



// cons [nam,setNam] = useState([]);
// cons [grad,setGrad] = useState([]);


function App() {
  
//  const postData = () =>{
//    axios.post('http://127.0.0.1:8000/student/',{
//       id : null,
//       name : stud_name,
//       grad : grade,
// }).then((respo) => setData(respo.data))
 
//  }

  const [data, setData] = useState([]);
  useEffect(() => {
    Axios.get('http://127.0.0.1:8000/student/').then((res) => setData(res.data));}, []);
   return (
    <div className="App">
      {data.map((value) => 
        
        
    <div>
         
           <p className="head">Student Name= {value.stud_name}</p> 
          <p>Grade= { value.grade}</p>
        <br></br>
          
        </div>
      
      )}
      
    {/* <form>
     <input  type="text" value={name} onChange={handle} />
     <input  type="text" value={grad} onChange={handleev} />


    </form> */}
    </div>
  );
}

export default App;


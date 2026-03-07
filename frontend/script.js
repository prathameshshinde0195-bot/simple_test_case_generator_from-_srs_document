async function upload(){

const file=document.getElementById("file").files[0]

if(!file){
  document.getElementById("result").innerText="Please select a PDF file first!"
  return
}

const formData=new FormData()

formData.append("file",file)

document.getElementById("result").innerText="Processing... Please wait..."

try{
  const response=await fetch("http://localhost:8000/generate",{
    method:"POST",
    body:formData
  })
  const data=await response.json()
  
  if(data.success){
    document.getElementById("result").innerText=data.result
  } else {
    document.getElementById("result").innerText="Error: " + data.error
  }
} catch(error){
  document.getElementById("result").innerText="Failed to connect to server: " + error.message + "\n\nMake sure the backend is running on http://localhost:8000"
}

}

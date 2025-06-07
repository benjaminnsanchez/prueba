fetch("https://prueba-4-6cgf.onrender.com")
.then(data => data.json())
.then(data => console.log(data[1]))

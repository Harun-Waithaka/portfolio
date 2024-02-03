  //document.getElementById("count-el").innerText =5

let saveEl = document.getElementById("save-el")
let countEl = document.getElementById("count-el")//Passing an argument 
console.log(countEl)
console.log(saveEl)

  let count = 0;
    function increment() {
      count += 1
     countEl.textContent = count 
    }
    //create a function  

    function save() {
        let countStr = count + " - "
        saveEl.textContent += countStr
        console.log(count)
        countEl.textContent = 0
        count = 0
        
    }
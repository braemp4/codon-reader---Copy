console.log("hello from index.js")

const fetchResidues = async (rna_seq) => {
      const res = await fetch("http://localhost:5000/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ seq: rna_seq })
      });
      const json = await res.json();
      return json["Peptide sequence"]
    };

    

const form = document.querySelector("#sequenceForm");
const resultBox = document.querySelector("#result")
form.addEventListener("submit", async (e) => {
    e.preventDefault(); //prevents page reload
    const formData = new FormData(form);
    const sequence = formData.get("sequence");
    //we need to now prevent calling fetchresidues if the sequence is invalid 
    const result = await fetchResidues(sequence);

    console.log(result)
    if (result && result.length > 0){
    resultBox.innerHTML = "Peptide Sequence: " + result
    
    }
    else {
        resultBox.innerHTML = ""
    }
})




 
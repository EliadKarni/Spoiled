const AZURE_URL = "https://spoiledservice.azurewebsites.net"
const SERIES_PATH = "series"

document.addEventListener("DOMContentLoaded",(event)=>{
    addSupportedSeries()

})
function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject(new Error(response.statusText))
    }
}

function displaySeries(jsonData){
    let seriesList = document.getElementById("seriesList")
    let id = 1
    jsonData.forEach((seriesName)=>{
        seriesList.innerHTML+=`
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="${id}_${seriesName}">
                <label class="form-check-label" for="series_1">${seriesName}</label>
            </div>
        `
        id++
    })
}

function addSupportedSeries(){
    fetch(`${AZURE_URL}/${SERIES_PATH}`)
        .then(status)
        .then(function(response) {
            return response.json();
        })
        .then(displaySeries)
        .catch(function(error){

        })

}
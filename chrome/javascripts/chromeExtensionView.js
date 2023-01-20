const AZURE_URL = "https://spoiledservice.azurewebsites.net"
const SERIES_PATH = "series"

const elementAndIdsModule = (function(){
    const HOME_PAGE_ID = "homePage"
    const CHOOSE_SERIES_BUTTON_ID = "chooseSeriesBtn"
    const SERIES_LIST_PAGE_ID = "seriesListPage"
    const FORM_SUBMISSION_SERIES_ID = "seriesListForm"
    const HOME_PAGE_ELEMENT = document.getElementById(HOME_PAGE_ID)
    const SERIES_LIST_PAGE_ELEMENT = document.getElementById(SERIES_LIST_PAGE_ID)
    const FORM_SUBMISSION_SERIES_ELEMENT = document.getElementById(FORM_SUBMISSION_SERIES_ID)

    return{
        HOME_PAGE_ELEMENT, CHOOSE_SERIES_BUTTON_ID, SERIES_LIST_PAGE_ELEMENT, SERIES_LIST_PAGE_ID,
        FORM_SUBMISSION_SERIES_ELEMENT, FORM_SUBMISSION_SERIES_ID, HOME_PAGE_ID
    }
})();



document.addEventListener("DOMContentLoaded",(event)=>{
    //addSupportedSeries()
    console.log("build listeners..")
    document.getElementById(elementAndIdsModule.CHOOSE_SERIES_BUTTON_ID).addEventListener("click",showSeries)
    elementAndIdsModule.FORM_SUBMISSION_SERIES_ELEMENT.addEventListener("submit",handleUserChoices)
    displaySeries()
})

function showSeries(_){
    elementAndIdsModule.HOME_PAGE_ELEMENT.classList.add("d-none")
    elementAndIdsModule.SERIES_LIST_PAGE_ELEMENT.classList.remove("d-none")
}

const fetchSeriesList = async ()=>{
    return new Promise((res)=>{
        chrome.storage.local.get(["seriesList"], (obj)=>{
            res(obj["seriesList"] ? obj["seriesList"]: [])
        });
    })
}

const displaySeries = async () =>{
    let series = await fetchSeriesList()
    let seriesList = document.getElementById("seriesList")
    let userChoicesString = await getUserChoices()
    userChoicesString = userChoicesString.join(" ")

    //will be changed to id from server.
    let id = 1
    series.forEach((seriesName)=>{
        seriesList.innerHTML+=`
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="${id}_${seriesName}" name="${id}_${seriesName}" 
                ${userChoicesString.includes(seriesName) ? `checked` : ""}>
                <label class="form-check-label" for="series_1">${seriesName}</label>
            </div>
        `
        id++
    })
}

const handleUserChoices = async(event)=>{
    event.preventDefault()
    let formData = new FormData(elementAndIdsModule.FORM_SUBMISSION_SERIES_ELEMENT);
    let userChoices = []
    for (const name of formData.keys()){
        userChoices.push(name)
    }
    await chrome.storage.local.set({["userChoices"]:JSON.stringify(userChoices)})
    elementAndIdsModule.HOME_PAGE_ELEMENT.classList.remove("d-none")
    elementAndIdsModule.SERIES_LIST_PAGE_ELEMENT.classList.add("d-none")
}

const getUserChoices = async () =>{
    return new Promise((res)=>{
        chrome.storage.local.get(["userChoices"], (obj)=>{
            res(obj["userChoices"] ? JSON.parse(obj["userChoices"]): [])
        });
    })
}


const AZURE_URL = "https://spoiledservice.azurewebsites.net"
const SERIES_PATH = "series"

chrome.runtime.onInstalled.addListener(details => {
    if (details.reason === "install")
        fetchList()
})

chrome.alarms.create("fetchListAlarm",{
    when: Date.now() + 1000,
    periodInMinutes: 60*24
})

chrome.alarms.onAlarm.addListener((alarm)=>{
    if (alarm.name === "fetchListAlarm")
        fetchList()
})

// move this code to utilities
function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject(new Error(response.statusText))
    }
}

function fetchList(){
    fetch(`${AZURE_URL}/${SERIES_PATH}`)
        .then(status)
        .then(function(response) {
            return response.json();
        })
        .then((list)=>{
                chrome.storage.local.set({'seriesList': list})
                    .then((item) => console.log(item))
            }
        )
        .catch((error) =>{
            console.log(error)
        })

}
// async function getCurrentTab() {
//     let queryOptions = { active: true, lastFocusedWindow: true };
//     let [tab] = await chrome.tabs.query(queryOptions);
//     return tab;
// }
chrome.tabs.onUpdated.addListener((tabId,changeInfo, tab)=>{
    if (changeInfo.status === 'complete'){
        chrome.scripting.executeScript({
            target: { tabId: tabId},
            files: ['pageImagesBlocker.js'],
        }).catch((err)=>{
            console.log(err)
        })
    }
})
// chrome.scripting.executeScript({
//             target: { tabId: await getCurrentTab().id},
//             files: ['pageImagesBlocker.js'],
//         }).catch((err)=>{
//         console.log(err)
// });


// chrome.webRequest.onBeforeRequest.addListener((details)=>{
//
//         if(details.type ==="image"){
//             return {redirectURL: chrome.runtime.getURL("../images/block.jpg")}
//         }
//
//     },
//     {
//         urls: ["<all_urls>"],
//         types: ["image"]
//     },
//     ["blocking"]
// )

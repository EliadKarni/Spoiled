(function(){
    const config = {childList: true, subtree:true}
    const changeImages = ()=>{
        console.log("============================here=============================")
        let srcElements = document.querySelectorAll('[src]');
        // let elementsWithImageOrVideoSrcArr = []
        // srcElements.forEach((elem)=>{
        //     if (elem.getAttribute('src').match())
        // })
        getServerResults (srcElements)
    }

    const getServerResults = (elements = []) =>{
        // temp implementation, will be change to server's check.
        elements.forEach((elem)=>{
            elem.setAttribute('src',chrome.runtime.getURL('../images/block.jpg'))
        })
    }

    let observer = new MutationObserver((mutations)=>{
        let relevantNewElements = []
        console.log("mutation")
        mutations.forEach((mutation)=>{
            mutation.addedNodes.forEach((node)=>{
                if (node.nodeType=== Node.ELEMENT_NODE && node.hasAttribute('src')){
                    relevantNewElements.push(node)
                }
            })
        })
        getServerResults(relevantNewElements)
    })
    if (typeof init === 'undefined'){
        const init = function(){
            changeImages()
            observer.observe(document,config)
        }
        init();
    }

    // document.addEventListener("DOMContentLoaded",(_)=>{
    //     changeImages()
    //     observer.observe(document,config)
    // })

})();
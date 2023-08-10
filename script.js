document.addEventListener("click", () => {
    const documentClickedEvent = new CustomEvent("document-clicked", {
        detail: {
            username: "ahmed0saber"
        }
    })

    document.dispatchEvent(documentClickedEvent)
})

document.addEventListener("click-listened", (event) => {
    console.log("JS: ", event)
})

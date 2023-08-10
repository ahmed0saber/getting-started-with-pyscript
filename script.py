from js import console, document, CustomEvent
from pyodide import create_proxy

def get_username(event):
    console.log("PY: ", event)
    click_listened_event = CustomEvent.new("click-listened", {"detail": {"username": "ahmed0saber"}})
    document.dispatchEvent(click_listened_event)


document.addEventListener("document-clicked", create_proxy(get_username))

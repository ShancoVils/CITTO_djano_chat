let number_group = document.querySelector("#room-id")
let bntFindRoom = document.querySelector("#btn-find-room")

bntFindRoom.addEventListener("click", () => {
    document.location.href ='/ws/chat/'+number_group.value;
    // const web_soket_local = new WebSocket('ws://' + window.location.host + '/ws/chat/'+number_group.value);
    // webSocket = web_soket_local
    // console.log(webSocket)
})
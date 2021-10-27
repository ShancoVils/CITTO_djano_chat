let chat = document.querySelector("#chat")
let chat_perent = document.querySelector("#chat-perent")
let input = document.querySelector("#message-input")
// let nickname = document.querySelector("#nickname")
let btnSubmit = document.querySelector("#btn-submit")
let header = document.querySelector(".display-3")

const roomName = JSON.parse(document.getElementById('room-name').textContent); 
console.log(roomName)


header.innerHTML  = '<h1 class="display-4">' + 'Комната: ' + roomName + '</h1>'

const webSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/'+roomName + '/');
console.log(webSocket)
 
webSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    chat.innerHTML += '<div class="msg">' + data.message + '</div>'
    chat_perent.scrollTop = block.scrollHeight;
    console.log("Новое сообщение")
    chat_perent.appendChild(chat)
 

};
 
 
btnSubmit.addEventListener("click", () => {
    // name_user = nickname.value;
    message = input.value;
    webSocket.send(JSON.stringify({
        // 'nickname': name_user,
        'message': message
    }));
    input.value = '';
})
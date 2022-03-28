import { io } from "socket.io-client";

class Socket {
  constructor() {
    if(process.env.NODE_ENV == "production"){
      this.server_host = window.location.origin
    }else{
      this.server_host = "http://127.0.0.1:5000";
    }
    this.socket = io(this.server_host);
  }

  connect() {
    this.socket.connect();
  }

  emitLogin(username, callback) {
    this.socket.emit("login", { username: username }, (result) => {
      if (callback) {
        callback(result);
      }
    });
  }

  onFriendOnline(callback){
		this.socket.on("friend online", (result) => {
			if(callback){
				callback(result)
			}
		})
  }

  onFriendOffline(callback){
    this.socket.on("friend offline", (result) => {
      if(callback){
        callback(result)
      }
    })
  }

  emitSendMessage(data, callback){
    this.socket.emit("send message", {"to": data['to'], "message": data['message']}, (result) => {
      if(callback){
        callback(result);
      }
    })
  }

  onReceiveMessage(callback){
    this.socket.on("receive message", (result) => {
      if(callback){
        callback(result);
      }
    })
  }

  get connected() {
    return this.socket.connected;
  }
}

export default new Socket();

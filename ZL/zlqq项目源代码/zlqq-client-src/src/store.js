import {createStore} from "vuex"

const store = createStore({
	state: {
		user: null,
		sessions: [], // {user, messages, unread}
		current_session: null
	},
	mutations: {
		SET_USER(state, user){
			state.user = user
		},
		ADD_SESSION(state, user){
			state.sessions.push({
				"user": user,
				"messages": [], // {content, date, self}
				"unread": 0
			})
		},
		DELETE_SESSION(state, user){
			for(let index=0; index<state.sessions.length; index++){
				let session = state.sessions[index];
				if(session.user.sid == user.sid){
					state.sessions.splice(index, 1);
					if(state.current_session.user.sid == session.user.sid){
						state.current_session = null;
					}
					break
				}
			}
		},
		SET_SESSIONS(state, users){
			const sessions = []
			for(let user of users){
				sessions.push({
					"user": user,
					"messages": [],
					"unread": 0
				})
			}
			state.sessions = sessions;
		},
		SET_CURRENT_SESSION(state, session){
			session.unread = 0;
			state.current_session = session;
		},
		SEND_MESSAGE(state, content){
			if(!state.current_session){
				return;
			}
			state.current_session.messages.push({
				content: content,
				date: (new Date()),
				self: true
			})
		},
		RECEIVE_MESSAGE(state, data){
			const sid = data['sid']
			const content = data['content']
			let chat_session = null
			for(let session of state.sessions){
				if(session.user.sid == sid){
					chat_session = session
					break
				}
			}
			if(chat_session){
				chat_session.messages.push({
					content: content,
					date: (new Date()),
					self: false
				})
				if(!state.current_session || 
					state.current_session.user.sid != chat_session.user.sid
				){
					chat_session.unread += 1
				}
			}
		}
	},
	getters: {
		logined(state){
			return state.user?true:false;
		}
	}
});


export default store;
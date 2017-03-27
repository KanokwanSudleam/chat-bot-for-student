var express = require('express');
var mongoose = require('mongoose');
var friendlist = require('../app/server/modules/friend')
var messagechat = require('../app/server/modules/message')
var socketio = require('socket.io');
//var db = require('./chat-db');
var router = express.Router();
var io;

router.listen = function(server) {
	console.log('Express server listening on port ' + server);
	io = socketio.listen(server);
	//io.set('log level', 2);
	io.on('connection', function(socket) {
		webinfor_bot(socket)
		normal_chat(socket)
		chatbot(socket)
		group_chat(socket)
	});

}

mongoose.connect('mongodb://127.0.0.1:27017/node-login', function(err) {
	if (err) {
		console.log(err);
	} else {
		console.log('Connect to mongodb')
	}
})



// var server = http.createServer(app).listen(app.get('port'), function() {
// 	console.log('Express server listening on port ' + app.get('port'));
// });
//var io = require('socket.io', { rememberTransport: false, transports: ['WebSocket', 'Flash Socket', 'AJAX long-polling'] })(server);
router.get('/', function(req, res) {

		res.send('hihihiiiihhiih')
	})
	// router.post('/webinfor/save', function(req, res) {

// 	var text = req.body.text
// 	var factory = req.body.factory1
// 	var announce = req.body.announce1
// 	var msg = {
// 		text: text,
// 		factory: factory,
// 		announce: announce,
// 		username: 'bot'
// 	}


// 	res.redirect('/webinfor');
// 	msg_web(msg)
// 	console.log(msg)

// })

// //console.log(msg)

// function msg_web(msg) {
// 	//webinfor_bot(socket, msg)


// }

function webinfor_bot(socket) {
	router.post('/webinfor/save', function(req, res) {

		var text = req.body.text
		var factory = req.body.factory1
		var announce = req.body.announce1
		var msg = {
			text: text,
			factory: factory,
			announce: announce,
			username: 'bot'
		}



		// msg_web(msg)
		console.log(msg)


		socket.removeAllListeners()
		socket.join('bot');
		io.sockets.in('bot').emit('what', {
			username: msg.username,
			message: msg.text + msg.factory + msg.announce
		});
		// socket.emit('chat', {
		// 	username: msg.username,
		// 	message: msg.text
		// });

		res.redirect('/webinfor');
	})

}


///////////////////////////////////////////////////////////////////////////////////////
// //send friend's name to webchat 
// app.post('/webchat', function(req, res) { //find old msg in room
// 	var room = req.body.room
// 	var fname = req.body.fname
// 	var myname = req.body.myname
// 	var text = { friend: fname, my: myname, room: room }
// 		// console.log(text)
// 	var find_msg = messagechat.findOne({ 'room': room }, function(err, data) {
// 		if (err) throw err;
// 		// console.log('find_sucess:', data.message)
// 		console.log(data.message)
// 		send_data(room, fname, myname, data.message)

// 	});
// 	//res.render('chat', text);
// 	function send_data(room, fname, myname, msgdata) {
// 		var text = { friend: fname, my: myname, room: room, msgdata: msgdata }
// 		res.render('chat', text);
// 		console.log("send_sucess", text)
// 	}
// });
////////////////////////////////////////////////////////////////////////////////////

//save new msg from client
function normal_chat(socket) {
	socket.removeAllListeners()
	socket.on('test', function(room) {

		socket.join(room.room);
		//console.log(room)
		save_message(room.room, room.username, room.message)
		if (room.room == 'chatbot') {
			io.sockets.in(room.room).emit('chat', room);
			py_msg(room.message, function(class_nlp) {
				//console.log(class_nlp)
				var new_data = {
					new_username: 'bot',
					new_message: room.message,
					nlp_msg: class_nlp
				}
				save_message(room.room, new_data.new_username, new_data.nlp_msg)
				io.sockets.in(room.room).emit('chat', new_data);
			})

		} else {
			if (room.message.slice(0, 4) === "@bot") {
				var msg_nlp = room.message.split("@bot");
				py_msg(msg_nlp[1], function(class_nlp) {
					//console.log(class_nlp)
					var bot_res = {
						new_username: 'bot',
						new_room: room.room,
						new_message: room.message,
						nlp_msg: class_nlp
					}
					console.log('show', bot_res)
					save_message(room.room, bot_res.new_username, bot_res.nlp_msg)
					io.sockets.in(room.room).emit('message', bot_res);
				})

			} else {
				io.sockets.in(room.room).emit('message', room);
			}

		}
	});
}
//////////group group group////////////
function group_chat(socket) {
	socket.removeAllListeners()
	socket.on('group', function(room) {
		socket.join(room.group);
		io.sockets.in(room.group).emit('group', room);
	});
}


////////// bot bot bot ////////////////
function chatbot(socket) {

	socket.on('wtf', function(data) {
		console.log(data)
		socket.join('bot');
		save_message(data.room, data.username, data.message)
		io.sockets.in('bot').emit('chat', data);
		py_msg(data.message, function(class_nlp) {
				//console.log(class_nlp)
				var new_data = {
					new_username: 'bot',
					new_message: data.message,
					nlp_msg: class_nlp
				}
				save_message(data.room, new_data.new_username, new_data.nlp_msg)
				io.sockets.in('bot').emit('chat', new_data);
			})
			// console.log(data.username, data.message)
			// socket.join(data.room);
			// io.sockets.in(data.room).emit('chat', data);
	})
}


function save_message(name_room, name_user, new_message) {
	var save_msg = messagechat.findOne({ 'room': name_room }, function(err, user) {
		//if (err) throw err;
		if (user == null) {
			var create_msg = new messagechat({ room: name_room, message: [{ name: name_user, msg: new_message }] });
			create_msg.save(function(err) {
				// we've saved the myfriend into the db here
				if (err) throw err;
				console.log('save sucess')
			});
		} else {
			var update_msg = messagechat.findOneAndUpdate({ room: name_room }, { $push: { "message": { name: name_user, msg: new_message } } }, { safe: true, upsert: true, new: true },
				function(err, user) {
					if (err) throw err;

					console.log('update_sucess')

				});




		}
	});
}

function py_msg(msg, class_msg) {
	var english = ["w", "e", "E", "r", "R", "t", "T", "y", "u", "U", "i", "I", "o", "p", "P", "[", "{", "]",
		"a", "A", "s", "S", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l", "L",
		";", ":", "q", "z", "x", "c", "C", "v", "V", "b", "n", "N", "m", ",", "<", ".", ">", "/", "?",
		"1", "4", "5", "6", "^", "7", "8", "9", "0", "-", "="
	]
	var thai = ["ไ", "ำ", "ฎ", "พ", "ฑ", "ะ", "ธ", "ั", "ี", "๊", "ร", "ณ", "น", "ย", "ญ", "บ", "ฐ", "ล", "ฟ",
		"ฤ", "ห", "ฆ", "ก", "ฏ", "ด", "โ", "เ", "ฌ", "้", "็", "่", "๋", "า", "ษ", "ส", "ศ", "ว", "ซ", "ง",
		"ผ", "ป", "แ", "ฉ", "อ", "ฮ", "ิ", "ื", "์", "ท", "ม", "ฒ", "ใ", "ฬ", "ฝ", "ฦ", "ๅ", "ภ", "ถ", "ุ", "ู", "ึ", "ค", "ต", "จ", "ข", "ช"
	]


	function include(arr, obj) {
		for (var i = 0; i < arr.length; i++) {
			if (arr[i] == obj) return true;
		}
	}

	function ThaiToEng(a) {
		//convert to array
		var temp = [];
		for (var i = 0; i < a.length; i++) {
			temp.push(a[i]);
		}
		//find index
		var index = []
		for (var i = 0; i < temp.length; i++) {
			if (include(thai, temp[i])) {
				index.push(thai.indexOf(temp[i]));
			}
		}
		//covert to englsh
		var b = "";
		for (var i = 0; i < index.length; i++) {
			b = b.concat(english[index[i]]);
		}
		return (b);
	}


	var spawn = require('child_process').spawn;
	var scriptExecution = spawn("python", ["script.py"]);
	// Handle normal output
	scriptExecution.stdout.on('data', function(data) {
		//console.log("what", String.fromCharCode.apply(null, data));
		class_msg(String.fromCharCode.apply(null, data));

	});

	// Write data (remember to send only strings or numbers, otherwhise python wont understand)
	//var data = JSON.stringify("ฝนตกมั๊ย");

	var data = JSON.stringify(ThaiToEng(msg));
	//console.log(data)
	scriptExecution.stdin.write(data);

	// End data write
	scriptExecution.stdin.end();

}
module.exports = router;

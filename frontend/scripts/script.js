

// init
var maxx = document.body.clientWidth;
var maxy = document.body.clientHeight;
var halfx = maxx / 2;
var halfy = maxy / 2;
var canvas = document.createElement("canvas");
document.body.appendChild(canvas);
canvas.width = maxx;
canvas.height = maxy;
var context = canvas.getContext("2d");
var dotCount = 200;
var dots = [];
// create dots
for (var i = 0; i < dotCount; i++) {
  dots.push(new dot());
}

// dots animation
function render() {
  context.fillStyle = "#000000";
  context.fillRect(0, 0, maxx, maxy);
  for (var i = 0; i < dotCount; i++) {
    dots[i].draw();
    dots[i].move();
  }
  requestAnimationFrame(render);
}

// dots class
// @constructor
function dot() {

  this.rad_x = 2 * Math.random() * halfx + 1;
  this.rad_y = 1.2 * Math.random() * halfy + 1;
  this.alpha = Math.random() * 360 + 1;
  this.speed = Math.random() * 100 < 50 ? 1 : -1;
  this.speed *= 0.1;
  this.size = Math.random() * 5 + 1;
  this.color = Math.floor(Math.random() * 256);

}

// drawing dot
dot.prototype.draw = function() {

  // calc polar coord to decart
  var dx = halfx + this.rad_x * Math.cos(this.alpha / 180 * Math.PI);
  var dy = halfy + this.rad_y * Math.sin(this.alpha / 180 * Math.PI);
  // set color
  context.fillStyle = "rgb(" + this.color + "," + this.color + "," + this.color + ")";
  // draw dot
  context.fillRect(dx, dy, this.size, this.size);

};

// calc new position in polar coord
dot.prototype.move = function() {

  this.alpha += this.speed;
  // change color
  if (Math.random() * 100 < 50) {
    this.color += 1;
  } else {
    this.color -= 1;
  }

};

// start animation
render();

for(var i = 0; i < 2; i++){
	parent_box = document.getElementById("third_info")
	card = document.getElementsByClassName("card")[0]
	if (card){
		card2 = card.cloneNode(true);
	parent_box.appendChild(card2)
	}
}
cards = document.getElementsByClassName("card")
for(var i = 0; i < cards.length; i++){
	cards[i].setAttribute("onmouseover", "change_style(" +i+ ")")
	cards[i].setAttribute("onmouseleave", "change_style2(" +i+ ")")
	header = cards[i].getElementsByClassName("card_header")[0]
	header.innerHTML = data[0][i]

	text = cards[i].getElementsByClassName("card_text")[0]
	text.innerHTML = data[1][i]

	card_img = cards[i].getElementsByClassName("card_img")[0]
	card_img.style.backgroundImage = "url("+data[2][i]+")"
}

function change_style(num){
	card_img = cards[num].getElementsByClassName('card_img')[0]
	card_img.style.opacity = 0.5;
	hidden_text = card_img.getElementsByClassName("card_hidden_text")[0]
	hidden_text.style.display = "block"
}

function change_style2(num){
	card_img = cards[num].getElementsByClassName('card_img')[0]
	card_img.style.opacity = 1;
	hidden_text = card_img.getElementsByClassName("card_hidden_text")[0]
	hidden_text.style.display = "none"
}

// fill_data()
// function fill_data() {
// 	js_block = document.getElementById("js_block")
// 	card2 = js_block.getElementsByClassName("card2")[0]
// 	for(var i = 0; i < data2.length; i++){
// 		for (var j = 0; j < data2[i].length; j++){
// 			newcard = card2.cloneNode(true)
// 			newcard.innerHTML = data2[i][j]
// 			js_block.appendChild(newcard)
// 		}
// 	}
// }

function get_data() {
    response = fetch("http://cerebrium.kz/api/data_finance/?name=arsen&id=5");
    response.json().then(data => {
        alert(data.fm)
    })
}

function register_user(){
	input_mail = document.getElementById("email")
	mail = input_mail.value
	input_password = document.getElementById("password")
	password = input_password.value
	"wedwedwedwed" + "333"
    response = fetch("/api/register_user?mail="+mail+"&password="+password);
    response.json().then(data => {
    })
}

function upload_track(){
	track = document.getElementById("track_input").value
	artist = document.getElementById('artist_input').value
	link = document.getElementById('link_input').value
    response = fetch("/api/find?trac="+trac+"&artist=" + artist + "&link=" + link);
    response.json().then(data => {
    })
}



musicBox = document.getElementById("music_box")
show_audio_tracks()
async function show_audio_tracks(){

    response = await fetch("/api/getplaylist");
    response.json().then(data => {
    	data_music = data.data_music
    	for (var i = 0; i < data_music.length; i++){
				artist = data_music[i][0]
				song_name = data_music[i][1]
				link = data_music[i][2]
 				orig = document.getElementById("original_audio")
 				newAudio = orig.cloneNode(true)
 				newAudio.getElementsByClassName("artist_name")[0].innerHTML = artist
 				newAudio.getElementsByClassName("song_name")[0].innerHTML = song_name
 				newAudio.getElementsByClassName("audio_source")[0].setAttribute("src" ,"/frontend/music/"+link)

			musicBox.appendChild(newAudio)
			console.log(musicBox, newAudio, orig)
		}
	})
}


function upload_track(){
 song_name = document.getElementById('song_name_input').value
 artist = document.getElementById('artist_input').value

 file_input = document.getElementById("file_input")

 data = new FormData()
 data.append('file', file_input.files[0])
 data.append('song_name', song_name)
 data.append('artist', artist)

 fetch('/api/upload_track/', {
   method: 'POST',
   body: data
 })
}

function upload_track(){
 song_name = document.getElementById('song_name_input').value
 artist = document.getElementById('artist_input').value
 console.log(song_name)
 file_input = document.getElementById("file_input")

 data = new FormData()
 data.append('file', file_input.files[0])
 data.append('song_name', song_name)
 data.append('artist', artist)
 csrf = document.getElementById('csrftoken').getAttribute('csrf')
 data.append('csrfmiddlewaretoken', csrf)

 fetch('/api/upload_track/', {
   method: 'POST',
   body: data
 })
}

function go_top() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
function go_end() {
  document.documentElement.scrollTop = document.documentElement.scrollHeight;
}
function go_hide(){
	$(".raw_log").hide();
}
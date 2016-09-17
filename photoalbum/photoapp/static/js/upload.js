function viewmypic(mypic,imgfile) {
	if (imgfile.value){
		mypic.src=imgfile.value;
		mypic.style.display="";
		mypic.border=1;
	}
	alert(mypic.src);
}
	  var imgW = 280;
	  var imgH = 455;
	  
      var stage = new Kinetic.Stage({
        container: 'container',
        width: imgW,
        height: imgH
      });
	  	  
      var imgOn = undefined;
      var imgOff = undefined;

      var layer = new Kinetic.Layer();
	  stage.add(layer);
      // add the layer to the stage    
	  
      var imageObjOn = new Image();
      imageObjOn.onload = function() {
        imgOn = new Kinetic.Image({
          x: 0,
          y: 0,
          image: imageObjOn,
		  width: imgW,
		  height:imgH
        });
        // add the shape to the layer
        layer.add(imgOn);	
		layer.draw();
      };	  
      imageObjOn.src = 'pic/on.jpg';

      var imageObjOff = new Image();
      imageObjOff.onload = function() {
        imgOff = new Kinetic.Image({
          x: 0,
          y: 0,
          image: imageObjOff,
		  width: imgW,
		  height: imgH
        });
        // add the shape to the layer
        layer.add(imgOff);	
		layer.draw();
      };	  
      imageObjOff.src = 'pic/off.jpg';
	  
	  var drawLight = function(isOn) {
	    if(isOn) {
		  imgOn.show();
		  imgOff.hide();
		} else {
		  imgOn.hide();
		  imgOff.show();
		}
		layer.draw();
	  }
	  

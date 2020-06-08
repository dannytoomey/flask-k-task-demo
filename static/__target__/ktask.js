'use strict';import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,__ipow__,
__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__proxy__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,filter,float,
getattr,hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import{fabric}from"./com.fabricjs.js";var __name__="__main__";export var orthoWidth=1E3;export var orthoHeight=750;export var fieldHeight=650;var __left0__=tuple([13,27,32]);export var enter=__left0__[0];export var esc=__left0__[1];export var space=
__left0__[2];window.onkeydown=function __lambda__(event){return event.keyCode!=space};export var Attribute=__class__("Attribute",[object],{__module__:__name__,get __init__(){return __get__(this,function(self,exp){self.exp=exp;self.exp.attributes.append(self);self.install();self.reset()})},get reset(){return __get__(this,function(self){self.commit()})},get predict(){return __get__(this,function(self){})},get interact(){return __get__(this,function(self){})},get commit(){return __get__(this,function(self){})},
get install(){return __get__(this,function(self){})}});export var Sprite=__class__("Sprite",[Attribute],{__module__:__name__,get __init__(){return __get__(this,function(self,exp,width,height){self.width=width;self.height=height;Attribute.__init__(self,exp)})},get install(){return __get__(this,function(self){self.image=new fabric.Rect(dict({"width":self.exp.scaleX(self.width),"height":self.exp.scaleY(self.height),"originX":"center","originY":"center","fill":"white"}))})},get reset(){return __get__(this,
function(self,vX,vY,x,y){if(typeof vX=="undefined"||vX!=null&&vX.hasOwnProperty("__kwargtrans__"))var vX=0;if(typeof vY=="undefined"||vY!=null&&vY.hasOwnProperty("__kwargtrans__"))var vY=0;if(typeof x=="undefined"||x!=null&&x.hasOwnProperty("__kwargtrans__"))var x=0;if(typeof y=="undefined"||y!=null&&y.hasOwnProperty("__kwargtrans__"))var y=0;if(arguments.length){var __ilastarg0__=arguments.length-1;if(arguments[__ilastarg0__]&&arguments[__ilastarg0__].hasOwnProperty("__kwargtrans__")){var __allkwargs0__=
arguments[__ilastarg0__--];for(var __attrib0__ in __allkwargs0__)switch(__attrib0__){case "self":var self=__allkwargs0__[__attrib0__];break;case "vX":var vX=__allkwargs0__[__attrib0__];break;case "vY":var vY=__allkwargs0__[__attrib0__];break;case "x":var x=__allkwargs0__[__attrib0__];break;case "y":var y=__allkwargs0__[__attrib0__];break}}}else;self.vX=vX;self.vY=vY;self.x=x;self.y=y;Attribute.reset(self)})},get commit(){return __get__(this,function(self){self.image.left=self.exp.orthoX(self.x);self.image.top=
self.exp.orthoY(self.y)})},get draw(){return __get__(this,function(self){self.exp.canvas.add(self.image)})}});export var Stimuli=__class__("Stimuli",[Sprite],{__module__:__name__,margin:60,width:50,height:50,get __init__(){return __get__(this,function(self,exp,index){self.index=index;Sprite.__init__(self,exp,self.width,self.height)})},get reset(){return __get__(this,function(self){Sprite.reset(self,__kwargtrans__({x:-orthoWidth/2+self.width+(orthoWidth-self.width)*Math.random(),y:-orthoHeight/2+self.height+
(orthoHeight-self.height)*Math.random()}))})}});export var Fixation=__class__("Fixation",[Sprite],{__module__:__name__,side:8,get __init__(){return __get__(this,function(self,exp){Sprite.__init__(self,exp,self.side,self.side)})}});export var Experiment=__class__("Experiment",[object],{__module__:__name__,get __init__(){return __get__(this,function(self){self.pause=true;self.keyCode=null;self.textFrame=document.getElementById("text_frame");self.canvasFrame=document.getElementById("canvas_frame");self.buttonsFrame=
document.getElementById("buttons_frame");self.canvas=new fabric.Canvas("canvas",dict({"backgroundColor":"grey","originX":"center","originY":"center"}));self.canvas.onWindowDraw=self.draw;self.canvas.lineWidth=2;self.canvas.clear();self.set_size=6;self.attributes=[];self.stimuli=function(){var __accu0__=[];for(var index=0;index<self.set_size;index++)__accu0__.append(Stimuli(self,index));return __accu0__}();self.fixation_point=Fixation(self);window.setInterval(self.py_update,1);window.setInterval(self.draw,
20);window.addEventListener("keydown",self.keydown);window.addEventListener("keyup",self.keyup);self.buttons=[];for(var key of tuple(["F","J","space"])){var button=document.getElementById(key);button.addEventListener("mousedown",function __lambda__(aKey){return function __lambda__(){return self.mouseOrTouch(aKey,true)}}(key));button.addEventListener("touchstart",function __lambda__(aKey){return function __lambda__(){return self.mouseOrTouch(aKey,true)}}(key));button.addEventListener("mouseup",function __lambda__(aKey){return function __lambda__(){return self.mouseOrTouch(aKey,
false)}}(key));button.addEventListener("touchend",function __lambda__(aKey){return function __lambda__(){return self.mouseOrTouch(aKey,false)}}(key));button.style.cursor="pointer";button.style.userSelect="none";self.buttons.append(button)}self.time=+new Date;self.start_exp_timer=self.time;self.target_presented=bool;self.isi_presented=bool;self.all_presented=bool;self.trial_set=bool;self.target_color=[];window.onresize=self.resize;self.resize()})},get install(){return __get__(this,function(self){for(var attribute of self.attributes)attribute.install()})},
get mouseOrTouch(){return __get__(this,function(self,key,down){if(down)if(key=="space")self.keyCode=space;else if(key=="enter")self.keyCode=enter;else self.keyCode=ord(key);else self.keyCode=null})},get py_update(){return __get__(this,function(self){var oldTime=self.time;self.time=+new Date;self.deltaT=(self.time-oldTime)/1E3;self.update_squares();if(self.pause){if(self.keyCode==space)self.pause=false}else{for(var attribute of self.attributes)attribute.predict();for(var attribute of self.attributes)attribute.interact();
for(var attribute of self.attributes)attribute.commit()}})},get update_squares(){return __get__(this,function(self){if(self.pause)for(var square of self.stimuli){if(square.image.fill!=self.canvas.backgroundColor)square.image.fill=self.canvas.backgroundColor}else{self.delta_exp_timer=self.time-self.start_exp_timer;if(self.delta_exp_timer<=1E3)if(self.trial_set!=true){for(var square of self.stimuli){square.reset();var red=255*Math.random();var green=255*Math.random();var blue=255*Math.random();var color=
"rgb({},{},{})".format(red,green,blue);square.image.fill=color;if(square==self.stimuli[0])self.target_color=square.image.fill}self.trial_set=true}if(1E3<self.delta_exp_timer&&self.delta_exp_timer<=1250)for(var square of self.stimuli)if(square.image.fill!=self.canvas.backgroundColor)square.image.fill=self.canvas.backgroundColor;if(1250<self.delta_exp_timer&&self.delta_exp_timer<=2E3)if(self.target_presented!=true){for(var square of self.stimuli)if(square.index>0)square.image.fill=self.canvas.backgroundColor;
else square.image.fill=self.target_color;self.target_presented=true}if(2E3<self.delta_exp_timer&&self.delta_exp_timer<=2500)for(var square of self.stimuli)if(square.image.fill!=self.canvas.backgroundColor)square.image.fill=self.canvas.backgroundColor;if(2500<self.delta_exp_timer){self.start_exp_timer=self.time;self.trial_set=false;self.target_presented=false;self.isi_presented=false;self.all_presented=false}}})},get commit(){return __get__(this,function(self){for(var attribute of self.attributes)attribute.commit()})},
get draw(){return __get__(this,function(self){self.canvas.clear();for(var attribute of self.attributes)attribute.draw()})},get resize(){return __get__(this,function(self){self.pageWidth=window.innerWidth;self.pageHeight=window.innerHeight;self.textTop=0;if(self.pageHeight>1.2*self.pageWidth){self.canvasWidth=self.pageWidth;self.canvasTop=self.textTop+300}else{self.canvasWidth=.6*self.pageWidth;self.canvasTop=self.textTop+200}self.canvasLeft=.5*(self.pageWidth-self.canvasWidth);self.canvasHeight=.6*
self.canvasWidth;self.buttonsTop=self.canvasTop+self.canvasHeight+50;self.buttonsWidth=500;self.textFrame.style.top=self.textTop;self.textFrame.style.left=self.canvasLeft+.05*self.canvasWidth;self.textFrame.style.width=.9*self.canvasWidth;self.canvasFrame.style.top=self.canvasTop;self.canvasFrame.style.left=self.canvasLeft;self.canvas.setDimensions(dict({"width":self.canvasWidth,"height":self.canvasHeight}));self.buttonsFrame.style.top=self.buttonsTop;self.buttonsFrame.style.left=.5*(self.pageWidth-
self.buttonsWidth);self.buttonsFrame.style.width=self.canvasWidth;self.install();self.commit();self.draw()})},get scaleX(){return __get__(this,function(self,x){return x*(self.canvas.width/orthoWidth)})},get scaleY(){return __get__(this,function(self,y){return y*(self.canvas.height/orthoHeight)})},get orthoX(){return __get__(this,function(self,x){return self.scaleX(x+Math.floor(orthoWidth/2))})},get orthoY(){return __get__(this,function(self,y){return self.scaleY(orthoHeight-Math.floor(fieldHeight/
2)-y)})},get keydown(){return __get__(this,function(self,event){self.keyCode=event.keyCode})},get keyup(){return __get__(this,function(self,event){self.keyCode=null})}});export var exp=Experiment();

//# sourceMappingURL=ktask.map
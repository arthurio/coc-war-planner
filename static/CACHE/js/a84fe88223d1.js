(function(){(function(jQuery){return jQuery.widget('IKS.hallorequireparagraphs',{options:{editable:null,uuid:'',blockElements:['dd','div','dl','figure','form','ul','ol','table','p','h1','h2','h3','h4','h5','h6']},cleanupContentClone:function(el){if(el.html().length&&!jQuery(this.options.blockElements.toString(),el).length){this.options.editable.execute('formatBlock','p');}}});})(jQuery);}).call(this);
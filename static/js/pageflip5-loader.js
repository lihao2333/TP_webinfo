/*
	Pageflip5 loader for Pageflip5 WordPress Plugin v1.1
*/

var pageflips = [],
	bookIDs = {},
	defaultBookID,
	loadedBookID,
	pageflip,
	$pageflip,
	$wrapper,

	
	registerPageflip = function ( pPFID, pCustomOptions, pBookID ) {
		
		var ID = pageflips.length;	//,
			//options = getOptions( pConfigOptions, pCustomOptions );
		
		if ( ID == 0 ) defaultBookID = pBookID;		//if this is the first Book, make it default
				
		pageflips[ ID ] = {	ID: ID, pfID: pPFID, bookID: pBookID,
							configOptions: mergeOptions( defaultConfigOptions, pCustomOptions ) 
							};
		bookIDs[ pBookID ] = ID;
		
		// returns a uniq ID
		return ID;
	},
	mergeOptions = function ( obj1, obj2 ) {
		var obj3 = {};
		for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
		for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
		return obj3;
	},
	startPageflip = function( id ) {
		if( id==loadedBookID ) return
		if( loadedBookID ) {
			//van mar pageflip-unk uh unload please!
			var pf = pageflips[ bookIDs[ loadedBookID ] ];
			pf.hash = location.hash;
			loadedBookID = undefined;
			pageflip.closePageflip( function() { startPageflip( id ); } );
			$wrapper.addClass("animated");
			
		} else {
			loadedBookID = id;

			var pf = pageflips[ bookIDs[ id ] ],
				$newwrapper = jQuery("#pageflip-wrapper"+pf.ID);
			$pageflip = jQuery("#"+pf.pfID);
			
			if( pf.hash ) {
				location.hash = pf.hash;
			} else {
				var h = getHashID();
				if( ( defaultBookID==id && h && h!=id ) || ( defaultBookID!=id && h!=id ) ) location.hash = id;
			}
			if( $wrapper ) {
				$wrapper.css( "height", $pageflip.css( "height" ) );
				$newwrapper.addClass("animated");
			}
			$wrapper = $newwrapper;
			
			$pageflip.pageflipInit( pf.configOptions, pf.bookID );
			$wrapper.css( "height", $pageflip.css( "height" ) );
			
			pageflip = $pageflip.pageflip();
			//pageflip.setPFEventCallBack( CustomPFEventHandler );
		}
		//onResize();
	},
	getHashID = function() {
		var h = location.hash;
		return h.substr( 1 ).split("/")[0];
	},
	
	id = getHashID();

	
jQuery( function() {
	
	var startBookID = defaultBookID;
	if( bookIDs[id]!=undefined && defaultBookID!=id ) {  startBookID = id; } 
	
	startPageflip( startBookID );
	
	jQuery(window).bind( "resize", function() {
		if( $wrapper && $pageflip ) {
			$wrapper.removeClass("animated");
			$wrapper.css( "height", $pageflip.css( "height" ) );
		}
	} );

});



	



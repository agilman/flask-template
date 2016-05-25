
function getLists(userId){
    return {'lists':['a','b','c']};
}

angular.module('ToDoApp', [])
.controller('ToDoAppController', ['$scope', function($scope) {
    angular.element(document).ready(function () {
	var userId = $("#userId");
	if (typeof userId != "undefined"){
	    var userId = $("#userId").val() 
	    $scope.userLists = getLists(userId);
	    
	}
    });
}]);

	    


(function(angular){
angular.module('myApp', [])
.controller('MyAppController', ['$scope','$http', function($scope,$http) {

    var userId = document.getElementById("userId").value;
    $scope.userId = userId;
    $http.get('/services/api/userLists/'+userId).then(function(data){
	$scope.toDoLists = data.data.lists;
	$scope.selectedList = 0;
	$scope.selectedListName = $scope.toDoLists[$scope.selectedList].name;
	$scope.$broadcast('listChangeBroadcast',$scope.selectedList);
    });

    $scope.$on('listSelectChangeEvent',function(event,data){
	$scope.selectedList = data;
	$scope.selectedListName = $scope.toDoLists[data].name;
	$scope.$broadcast('listChangeBroadcast',data);
    });

}])
.controller('ToDoListsController',['$scope',function($scope){
    $scope.getChecked = function(indx){
	var items = $scope.toDoLists[indx].items;
	var checkedCount = 0;
	for (var i=0;i<items.length; i++){
	    if (items[i].completed){
		checkedCount+=1;
	    }
	}
	return checkedCount.toString();
    };    
    $scope.getTotal = function(indx){
	var total = $scope.toDoLists[indx].items.length;
	return total.toString();
    };
    $scope.toDoClick = function(indx){
	$scope.$emit('listSelectChangeEvent',indx);
    };

}])
.controller('ToDoItemsController',['$scope','$http',function($scope,$http){
    $scope.checkMark = function(indx){
        if ($scope.items[indx].completed){
	    return "check";
	}else{
	    return "unchecked";
	}
    };

    $scope.$on("listChangeBroadcast",function(event,data){
	if ($scope.toDoLists.length==0){
	    $scope.items=[];
	}
	$scope.items = $scope.toDoLists[data].items;
    });
}]);
})(window.angular);

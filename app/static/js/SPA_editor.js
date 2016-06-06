
function getLists(){
    return [{'id':1,
	     'name':"Programming Skills",
	     'items':[{'id':1,
		       'name':'Learn Python',
		       'checked':true},
		      {'id':2,'name':'Learn Flask','checked':true},
			  {'id':3,'name':'Learn Bootstra','checked':false},
			  {'id':4,'name':'Learn Angular','checked':false},
			  {'id':5,'name':'Learn Node.js','checked':false}]},
	    {'id':2,
	     'name':"Life Goals",
	     'items':[{'id':6,
		       'name':'Buy a van',
		       'checked':false},
		      {'id':7,
		       'name':'Live by the river',
		       'checked':false
		      }]
	    }];
}


(function(angular){
angular.module('myApp', [])
.controller('MyAppController', ['$scope', function($scope) {
    $scope.toDoLists = getLists();
    $scope.selectedList = 0;
    $scope.$on('listSelectChangeEvent',function(event,data){
	$scope.selectedList = data;
	$scope.$broadcast('listChangeBroadcast',data);
    });
}])
.controller('ToDoListsController',['$scope',function($scope){
    $scope.getChecked = function(indx){
	var items = $scope.toDoLists[indx].items;
	var checkedCount = 0;
	for (var i=0;i<items.length; i++){
	    if (items[i].checked){
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
.controller('ToDoItemsController',['$scope',function($scope){
    $scope.items = $scope.toDoLists[$scope.selectedList].items;
    $scope.checkMark = function(indx){
        if ($scope.items[indx].checked){
	    return "check";
	}else{
	    return "unchecked";
	}
    };
    $scope.$on("listChangeBroadcast",function(event,data){
	$scope.items = $scope.toDoLists[data].items;
    })
}]);
})(window.angular);

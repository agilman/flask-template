
function getLists(){
    return [{'id':1,
	     'name':"Programming Skills",
	     'items':[{'id':1,'name':'Learn Python','checked':true},
		      {'id':2,'name':'Learn Flask','checked':true},
		      {'id':3,'name':'Learn Bootstrap','checked':false},
		      {'id':4,'name':'Learn Angular','checked':false},
		      {'id':5,'name':'Learn Node.js','checked':false}]},
	    {'id':2,
	     'name':"Life Goals",
	     'items':[{'id':6,'name':'Buy a van', 'checked':false},
		      {'id':7,'name':'Live by the river','checked':false }]
	    }];
}

(function(angular){
angular.module('myApp', [])
.controller('MyAppController', ['$scope', function($scope) {
    $scope.toDoLists = getLists();
    $scope.selectedList = 0;
    $scope.selectedListName = $scope.toDoLists[$scope.selectedList].name;
    $scope.addListClick = function(name){
	$scope.newListName="";
	var newList = {'name':name,'items':[] };
	$scope.toDoLists.push(newList);

	//select newly create item
	$scope.selectedList=$scope.toDoLists.length-1;
	$scope.selectedListName=name;
	$scope.$broadcast('listChangeBroadcast',$scope.selectedList);
    };
    $scope.addItemClick = function(name){
	var newItem = {'name':name,'checked':false};
	$scope.newItemName="";
	$scope.toDoLists[$scope.selectedList].items.push(newItem);
    };
    $scope.$on('listSelectChangeEvent',function(event,data){
	$scope.selectedList = data;
	$scope.selectedListName = $scope.toDoLists[data].name;
	$scope.$broadcast('listChangeBroadcast',data);
    });
    $scope.$on('checkClickEvent',function(event,data){
	if ($scope.toDoLists[$scope.selectedList].items[data].checked==true){
	    $scope.toDoLists[$scope.selectedList].items[data].checked=false;
	}else{
	    $scope.toDoLists[$scope.selectedList].items[data].checked=true;
	}
    });
    $scope.$on('removeListEvent',function(event,data){
	$scope.toDoLists.splice(data,1);
	if (data==$scope.selectedList){
	    $scope.selectedList=0;

	    if ($scope.toDoLists.length>0){
		$scope.selectedListName=$scope.toDoLists[0].name;
	    }else{
		$scope.selectedListName="";
	    }
	    $scope.$broadcast('listChangeBroadcast',0);	    
	}
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
    $scope.removeListClick = function(indx){
	$scope.$emit('removeListEvent',indx);
    };
}])
.controller('ToDoItemsController',['$scope',function($scope){
    $scope.items = $scope.toDoLists[$scope.selectedList].items;
    $scope.checkClick = function(indx){
	$scope.$emit('checkClickEvent',indx);
    };
    $scope.checkMark = function(indx){
        if ($scope.items[indx].checked){
	    return "check";
	}else{
	    return "unchecked";
	}
    };
    $scope.itemRemoveClick = function(indx){
	$scope.items.splice(indx,1);
    };
    $scope.$on("listChangeBroadcast",function(event,data){
	if ($scope.toDoLists.length==0){
	    $scope.items=[];
	}
	$scope.items = $scope.toDoLists[data].items;
    });
}]);
})(window.angular);

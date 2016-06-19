
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

    $scope.addListClick = function(name){
	//prepare json to pass
	var newList = {'userId':$scope.userId,'name':name};

	$http.post('/services/api/lists',JSON.stringify(newList)).then(function(data){
	    var rList = data.data.newList;
	    rList["items"]=[];
	    $scope.toDoLists.push(rList);
	    
	    //select newly create item
	    $scope.selectedList=$scope.toDoLists.length-1;
	    $scope.selectedListName=name;
	    $scope.$broadcast('listChangeBroadcast',$scope.selectedList);
	});

	//clear value
	$scope.newListName="";	
    }

    $scope.addItemClick = function(name){
	var listId = $scope.toDoLists[$scope.selectedList].id;
	var newItem = {'listId':listId,'task':name,'completed':false};
	$http.post('/services/api/listItems',JSON.stringify(newItem)).then(function(data){
	    var nItem = data.data.newItem;
	    $scope.toDoLists[$scope.selectedList].items.push(nItem);
	});

	//clear name
	$scope.newItemName="";
    };

    $scope.$on('listSelectChangeEvent',function(event,data){
	$scope.selectedList = data;
	$scope.selectedListName = $scope.toDoLists[data].name;
	$scope.$broadcast('listChangeBroadcast',data);
    });

    $scope.$on('checkClickEvent',function(event,indx){
	var item = $scope.toDoLists[$scope.selectedList].items[indx];
	var itemId = item.id;
	
	var oldValue = item.completed;
	var newValue = !oldValue;
	
	var update = {'id':itemId,'completed':newValue};
	$http.put('/services/api/listItems',JSON.stringify(update)).then(function(data){
	    $scope.toDoLists[$scope.selectedList].items[indx].completed=newValue;
	});

    });

    $scope.$on('removeListEvent',function(event,indx){
	var listId = $scope.toDoLists[indx].id;
	$http.delete('/services/api/lists/'+listId).then(function(resp){
	    $scope.toDoLists.splice(indx,1);
	   
	    //if removing the list that is being displayed, select another list to display
	    if (indx==$scope.selectedList){
		$scope.selectedList=0;
		
		if ($scope.toDoLists.length>0){
		    $scope.selectedListName=$scope.toDoLists[0].name;
		}else{
		    $scope.selectedListName="";
		}
		$scope.$broadcast('listChangeBroadcast',0);	    
	    }
	});
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
    $scope.removeListClick = function(indx){
	$scope.$emit('removeListEvent',indx);
    };
}])
.controller('ToDoItemsController',['$scope','$http',function($scope,$http){
    $scope.checkClick = function(indx){
	$scope.$emit('checkClickEvent',indx);
    };

    $scope.checkMark = function(indx){
        if ($scope.items[indx].completed){
	    return "check";
	}else{
	    return "unchecked";
	}
    };

    $scope.itemRemoveClick = function(indx){
	var itemId = $scope.items[indx].id;
	
	$http.delete('/services/api/listItems/'+itemId).then(function(resp){
	    $scope.items.splice(indx,1);
	});
    };

    $scope.$on("listChangeBroadcast",function(event,data){
	if ($scope.toDoLists.length==0){
	    $scope.items=[];
	}
	$scope.items = $scope.toDoLists[data].items;
    });
}]);
})(window.angular);

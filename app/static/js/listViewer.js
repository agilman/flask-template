function getLists(userId){
    return ["First List","SecondLIst","Another"];
}

(function(angular){
angular.module('ToDoApp', [])
.controller('listController', ['$scope', function($scope) {
    $scope.lists = getLists(1);
}]);

})(window.angular);	    

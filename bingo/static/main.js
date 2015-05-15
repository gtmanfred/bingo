var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;

  // an array that will be populated with substring matches
    matches = [];

  // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');

  // iterate through the pool of strings and for any string that
  // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);
  };
};

var myApp = angular.module('bingo', []);

myApp.controller('BingoController', ['$scope', '$log', '$http', function($scope, $log, $http) {
  $scope.ruleForm = {
      "name": "",
      "value": "",
  };
  function get_rules(){
    $http.get('/rules').
      success(function(data, status, headers, config) {
        $scope.rules = data['rules'];
        var ruleNames = Object.keys(data['rules']);
        $('#ruleName').autocomplete({source: $scope.ruleNames});
        var names = [];
        var tmpname = [];
        for (var x in ruleNames) {
          tmpname.push(ruleNames[x]);
          if (tmpname.length == 5) {
              names.push(tmpname);
              tmpname = [];
          };
        };
        names.push(tmpname);
        $scope.ruleTableNames = names;
        $scope.ruleNames = ruleNames;
      }).error(function(error) {
        $log.log(error);
      });
  };
  function reset_buttons(){
    for(var rule in $scope.rules) {
      if ($scope.rules[rule].active) {
        $http.put('/rules/' + rule).
          success(function(data, status, headers, config) {
              get_rules();
          }).error(function(error){$log.log(error);});
      };
    }
  };
  $scope.entry = function() {
    if ($scope.ruleNames.indexOf($scope.ruleForm.name) > -1) {
      $http.put('/rules', data=$scope.ruleForm).
        success(function() {
          location.reload();
        }).error(function(error){$log.log(error)});
    } else {
      $http.post('/rules', data=$scope.ruleForm).
        success(function() {
          location.reload();
        }).error(function(error){$log.log(error)});
    };
  }
  $(document).on("click", "button.rule", function () {
    $http.put('/rules/' + this.name).
      success(function(data, status, headers, config) {
          get_rules();
      }).error(function(error){$log.log(error);});
  });
  $(document).on("focusout", "input.entry", function () {
    if ($scope.ruleNames.indexOf($scope.ruleForm.name) > -1) {
      $scope.ruleForm.value = $scope.rules[$scope.ruleForm.name].rule;
    }
  });
  $(document).on("click", "a.reset", function () {
    reset_buttons();
  });
  get_rules();
  setInterval(function(){get_rules()}, 30000);
}]);

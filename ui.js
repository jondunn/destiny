/**
 * @author Daniel Reed &lt;<a href="mailto:n@ml.org">n@ml.org</a>&gt;
 */

(function() {

/** @namespace */
nmlorg = window.nmlorg || {};


/** @namespace */
nmlorg.ui = nmlorg.ui || {};


nmlorg.ui.character = function(character) {
  var div = document.createElement('div');
  div.className = 'emblem';
  div.style.backgroundImage = "url('https://www.bungie.net" + character.emblem_banner + "')";

  var img = document.createElement('img');
  div.appendChild(img);
  img.src = 'https://www.bungie.net' + character.emblem_icon;

  var classDiv = document.createElement('div');
  div.appendChild(classDiv);
  classDiv.className = 'class';
  classDiv.textContent = character.class;

  var subDiv = document.createElement('div');
  div.appendChild(subDiv);
  subDiv.className = 'subtitle';
  subDiv.textContent = character.race + ' ' + character.gender;

  var levelDiv = document.createElement('div');
  div.appendChild(levelDiv);
  levelDiv.className = 'level';
  levelDiv.textContent = character.level;

  var lightDiv = document.createElement('div');
  div.appendChild(lightDiv);
  lightDiv.className = 'light';
  lightDiv.textContent = '\u2666 ' + character.light;

  var statsDiv = document.createElement('div');
  div.appendChild(statsDiv);
  statsDiv.className = 'stats';
  var norm = (character.stats.Agility + character.stats.Armor + character.stats.Recovery) / 100;
  var stats = [[100 + Math.round(character.stats.Agility / norm), 'Agility'],
               [100 + Math.round(character.stats.Armor / norm), 'Armor'],
               [100 + Math.round(character.stats.Recovery / norm), 'Recovery']];
  stats.sort();
  statsDiv.textContent = stats[2][1] + ' > ' + stats[1][1] + ' > ' + stats[0][1];
  statsDiv.title = (stats[2][0] - 100) + '% > ' + (stats[1][0] - 100) + '% > ' + (stats[0][0] - 100) + '%';

  return div;
};


nmlorg.ui.item = function(item) {
  var div = document.createElement('a');
  div.className = 'item';
  div.href = '/db/InventoryItem/' + item.hash;

  var img = document.createElement('img');
  div.appendChild(img);
  img.src = 'https://www.bungie.net' + item.icon;

  if (item.quantity > 1) {
    var quantityDiv = document.createElement('div');
    div.appendChild(quantityDiv);
    quantityDiv.className = 'quantity';
    quantityDiv.textContent = item.quantity;
  }

  var titleDiv = document.createElement('div');
  div.appendChild(titleDiv);
  titleDiv.className = 'title';
  titleDiv.textContent = item.name;

  var subtitleDiv = document.createElement('div');
  div.appendChild(subtitleDiv);
  subtitleDiv.className = 'subtitle';
  subtitleDiv.textContent = item.type;
  var subs = [];
  if (item.class)
    subs.push(item.class)
  if (item.tier && (item.tier != 'Common'))
    subs.push(item.tier);
  if (subs.length) {
    subs.sort();
    subtitleDiv.textContent += ' (' + subs.join(', ') + ')';
  }

  var statDiv = document.createElement('div');
  div.appendChild(statDiv);
  statDiv.className = 'stat';
  if (item.primary_stat_value)
    statDiv.textContent = item.primary_stat_value;

  var statTypeDiv = document.createElement('div');
  div.appendChild(statTypeDiv);
  statTypeDiv.className = 'stat-type';
  if (item.damage_type)
    statTypeDiv.textContent = item.damage_type[0].toUpperCase() + item.damage_type.substr(1).toLowerCase() + ' ';
  else if (item.primary_stat_type)
    statTypeDiv.textContent += item.primary_stat_type;

  div.title = titleDiv.textContent + (item.quantity > 1 ? ' (x ' + item.quantity + ')' : '') + '\n' +
      subtitleDiv.textContent + '\n' +
      statDiv.textContent + ' ' + statTypeDiv.textContent + (item.fully_upgraded ? '' : ' (in progress)') + '\n' +
      '\n' + item.desc;

  return div;
};


nmlorg.ui.quest = function(quest) {
  var parent = document.createElement('div');

  var div = document.createElement('div');
  parent.appendChild(div);
  div.className = 'quest';

  var img = document.createElement('img');
  div.appendChild(img);
  img.src = 'https://www.bungie.net' + quest.icon;

  var titleDiv = document.createElement('div');
  div.appendChild(titleDiv);
  titleDiv.className = 'title';
  titleDiv.textContent = quest.name;

  var subtitleDiv = document.createElement('div');
  div.appendChild(subtitleDiv);
  subtitleDiv.className = 'subtitle';
  subtitleDiv.textContent = quest.desc;

  div.title = titleDiv.textContent + '\n\n' + quest.desc;

  for (var i = 0; i < quest.steps.length; i++)
    parent.appendChild(nmlorg.ui.questStep(quest.steps[i]));

  return parent;
};


nmlorg.ui.questStep = function(step) {
  var div = document.createElement('a');
  div.className = 'quest-step';
  if (step.active)
    div.className += ' active';
  div.href = '/db/InventoryItem/' + step.hash;
  div.textContent = step.objective;
  div.title = step.name + '\n\n' + step.objective + '\n';
  for (var i = 0; i < step.objectives.length; i++) {
    var objective = step.objectives[i];
    if (objective.count > 1)
      div.title += '- ' + objective.count + ' ' + objective.name + '\n';
    else
      div.title += '- ' + objective.name + '\n';
  }
  div.title += '\n' + step.desc;
  return div;
};

})();

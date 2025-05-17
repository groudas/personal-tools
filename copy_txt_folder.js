const fs = require('fs');
const path = require('path');

const rootDir = process.cwd();
const rootBaseName = path.basename(rootDir);
const parentDir = path.dirname(rootDir);
const copiedDirName = rootBaseName + 'copy';
const copiedDirPath = path.join(parentDir, copiedDirName);

if (!fs.existsSync(copiedDirPath)) {
  fs.mkdirSync(copiedDirPath);
  console.log(`Diretório de destino criado: "${copiedDirPath}"`);
} else {
    console.log(`Diretório de destino já existe: "${copiedDirPath}"`);
}

let treeOutputLines = [];

function buildTreeStructure(currentDir, depth) {
  const entries = fs.readdirSync(currentDir);
    const indentation = '  '.repeat(depth);

    entries.sort();

  for (const entry of entries) {
    const fullPath = path.join(currentDir, entry);
    const stats = fs.statSync(fullPath);

    if (stats.isDirectory()) {
            treeOutputLines.push(`${indentation}${entry}/`);
            buildTreeStructure(fullPath, depth + 1);
    } else if (stats.isFile()) {
            treeOutputLines.push(`${indentation}${entry}`);
        }
    }
}

function processDirRecursive(currentDir) {
  const entries = fs.readdirSync(currentDir);

  for (const entry of entries) {
    const fullPath = path.join(currentDir, entry);
    const stats = fs.statSync(fullPath);

    if (stats.isDirectory()) {
      processDirRecursive(fullPath);
    } else if (stats.isFile()) {
      try {
        const relativePath = path.relative(rootDir, fullPath);

        const newFileName = relativePath.replace(new RegExp('\\' + path.sep, 'g'), '_') + '.txt';

        const destFilePath = path.join(copiedDirPath, newFileName);

        const fileContent = fs.readFileSync(fullPath, 'utf8');

        fs.writeFileSync(destFilePath, fileContent);


      } catch (error) {
        console.error(`Error processing file "${fullPath}": ${error.message}`);
      }
    }
  }
}

console.log(`Iniciando cópia e conversão de arquivos de "${rootDir}" para "${copiedDirPath}"...`);

try {
  processDirRecursive(rootDir);
  console.log('Cópia e conversão concluídas.');


  console.log('Gerando estrutura de diretórios...');
  treeOutputLines.push('.');
  buildTreeStructure(rootDir, 0);


  const treeOutputString = treeOutputLines.join('\n');
  const treeFileName = 'tree_structure.txt';
  const treeFilePath = path.join(copiedDirPath, treeFileName);

  fs.writeFileSync(treeFilePath, treeOutputString, 'utf8');
  console.log(`Estrutura de diretórios exportada para "${treeFilePath}"`);

} catch (error) {
  console.error('Erro durante o processo:', error);
}
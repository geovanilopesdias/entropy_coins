package entropia_moedas1;

import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
import java.lang.Math;
/**
 * @author Geovani
 */
public class Entropia_moedas1 {

    public static void main(String[] args) {
        int m, l, trad;
        double conf;
        Scanner t = new Scanner(System.in);
        System.out.print("Insira o número de moedas a sortear (maior que um): ");
        m = Integer.parseInt(t.nextLine());
        while (m < 2) {
            System.out.print("Apenas valores maiores que um são válidos: ");
            m = Integer.parseInt(t.nextLine());
        }
        System.out.print("Insira quantas vezes devem ser lançadas cada uma (maior que um): ");
        l = Integer.parseInt(t.nextLine());
        while (l < 2) {
            System.out.print("<html><b>Apenas valores maiores que um são válidos: </b></html>");
            l = Integer.parseInt(t.nextLine());
        }
        conf = (Math.pow(m, 2)-m)/2; // Conferências por lançamento
        char [][]sGeral = new char[m][l];
        
        // Execução dos lançamentos:
        for (int x = 0; x < m; x++){
            for (int y = 0; y < l; y++){
                trad = ThreadLocalRandom.current().nextInt(1, 3);
                if (trad == 1){ // Cara
                    sGeral[x][y] = 'X';
                } else { // Coroa
                    sGeral[x][y] = '0';
                }
            }
        }
        if ((m <=10)&&(l<=10)){
            for (int x = 0; x < m; x++){
                for (int y = 0; y < l; y++){
                    System.out.println((x+1)+"ª moeda, "+(y+1)+"º lançamento: "+
                            sGeral[x][y]);
                }
            }
        }
        int repetPar=0, repetGlobal=0, a=0, b=a+1;
        for (int lanc=0; lanc < l; lanc++){
            while (true){
                while (true){
                    if (sGeral[a][lanc] == sGeral[b][lanc]){
                        repetPar++;
                    }
                    if (repetPar == conf){
                        repetGlobal++;
                    }
                    if (b == (m-1)){
                        break;
                    } else {
                        b++;
                    }
                }
                if (a == m-2){
                    repetPar = 0;
                    a = 0;
                    b = a+1;
                    break;
                } else {
                    a++;
                    b = a+1;
                }
            }
        }
        String sinplu = ((repetGlobal == 1)||(repetGlobal == 0)) ? "":"es"; // Variável para concordância
        System.out.println("As "+m+" moedas caíram todas iguais "+repetGlobal+" vez"+sinplu);
        double prob = Math.pow((2/(Math.pow(2, m))), -1);
        if (repetGlobal != 0) {
            System.out.println("A probabilidade do ocorrido é de uma em "+prob*repetGlobal);
        }
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;

/**
 *
 * @author Roshan Withanage
 */
public class ControlStructuresModel {

    private int lineNo;
    private String programStatement;
    private int Wtcs;
    private int NC;
    private int Ccspps;
    private int Ccs;

    public ControlStructuresModel() {
    }

    public ControlStructuresModel(int lineNo, String programStatement, int Wtcs, int NC, int Ccspps, int Ccs) {
        this.lineNo = lineNo;
        this.programStatement = programStatement;
        this.Wtcs = Wtcs;
        this.NC = NC;
        this.Ccspps = Ccspps;
        this.Ccs = Ccs;
    }

    public int getLineNo() {
        return lineNo;
    }

    public void setLineNo(int lineNo) {
        this.lineNo = lineNo;
    }

    public String getProgramStatement() {
        return programStatement;
    }

    public void setProgramStatement(String programStatement) {
        this.programStatement = programStatement;
    }

    public int getWtcs() {
        return Wtcs;
    }

    public void setWtcs(int Wtcs) {
        this.Wtcs = Wtcs;
    }

    public int getNC() {
        return NC;
    }

    public void setNC(int NC) {
        this.NC = NC;
    }

    public int getCcspps() {
        return Ccspps;
    }

    public void setCcspps(int Ccspps) {
        this.Ccspps = Ccspps;
    }

    public int getCcs() {
        return Ccs;
    }

    public void setCcs(int Ccs) {
        this.Ccs = Ccs;
    }

}
